import argparse
import asyncio
import contextlib
import json
import os
import random
import sys
import time
from functools import partial
from Runners.Executors.console import Swdconsole_logs, errors
from typing import Dict
from typing import List
from typing import Union

import httpx
import regex
import requests

err = Swdconsole_logs()

BING_URL = os.getenv("BING_URL", "https://www.bing.com")

FORWARDED_IP = (
    f"13.{random.randint(104, 107)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
)
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "content-type": "application/x-www-form-urlencoded",
    "referrer": "https://www.bing.com/images/create/",
    "origin": "https://www.bing.com",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
    "x-forwarded-for": FORWARDED_IP,
}

sending_message = "Sending request..."
wait_message = "Waiting for results..."
download_message = "\nDownloading images..."


def debug(debug_file, text_var):
    with open(f"{debug_file}", "a", encoding="utf-8") as f:
        f.write(str(text_var))
        f.write("\n")

class ImageGen:
    def __init__(
        self,
        auth_cookie: str,
        auth_cookie_SRCHHPGUSR: str,
        debug_file: Union[str, None] = None,
        quiet: bool = False,
        all_cookies: List[Dict] = None,
    ) -> None:
        self.session: requests.Session = requests.Session()
        self.session.headers = HEADERS
        self.session.cookies.set("_U", auth_cookie)
        self.session.cookies.set("SRCHHPGUSR", auth_cookie_SRCHHPGUSR)
        if all_cookies:
            for cookie in all_cookies:
                self.session.cookies.set(cookie["name"], cookie["value"])
        self.quiet = quiet
        self.debug_file = debug_file
        if self.debug_file:
            self.debug = partial(debug, self.debug_file)

    async def get_images(self, prompt: str, channel, user) -> list:
        if not self.quiet:
            print(sending_message)
        if self.debug_file:
            self.debug(sending_message)
        url_encoded_prompt = requests.utils.quote(prompt)
        payload = f"q={url_encoded_prompt}&qs=ds"
        # https://www.bing.com/images/create?q=<PROMPT>&rt=3&FORM=GENCRE
        url = f"{BING_URL}/images/create?q={url_encoded_prompt}&rt=4&FORM=GENCRE"
        response = self.session.post(
            url,
            allow_redirects=False,
            data=payload,
            timeout=200,
        )

        if "this prompt is being reviewed" in response.text.lower():
            if self.debug_file:
                self.debug(f"ERROR: {errors.prompt_being_reviewed_error}")
            await err.channel_error('800', channel, user)
            raise Exception(
                errors.prompt_being_reviewed_error,
            )
        if "this prompt has been blocked" in response.text.lower():
            if self.debug_file:
                self.debug(f"ERROR: {errors.blocked_prompt_error}")
            await err.channel_error('700', channel, user)
            raise Exception(
                errors.blocked_prompt_error,
            )
        if (
            "we're working hard to offer image creator in more languages"
            in response.text.lower()
        ):
            if self.debug_file:
                self.debug(f"ERROR: {errors.unsupported_lang_error}")
            await err.channel_error('1000', channel, user)
            raise Exception(errors.unsupported_lang_error)
        if response.status_code != 302:

            url = f"{BING_URL}/images/create?q={url_encoded_prompt}&rt=3&FORM=GENCRE"
            response = self.session.post(url, allow_redirects=False, timeout=200)
            if response.status_code != 302:
                if self.debug_file:
                    self.debug(f"ERROR: {errors.redirect_error}")
                print(f"ERROR: {response.text}")
                await err.channel_error('600', channel, user)
                raise Exception(errors.redirect_error)

        redirect_url = response.headers["Location"].replace("&nfy=1", "")
        request_id = redirect_url.split("id=")[-1]
        self.session.get(f"{BING_URL}{redirect_url}")
        # https://www.bing.com/images/create/async/results/{ID}?q={PROMPT}
        polling_url = f"{BING_URL}/images/create/async/results/{request_id}?q={url_encoded_prompt}"

        if self.debug_file:
            self.debug("Polling and waiting for result")
        if not self.quiet:
            print("Waiting for results...")
        start_wait = time.time()
        while True:
            if int(time.time() - start_wait) > 200:
                if self.debug_file:
                    self.debug(f"ERROR: {errors.timeout_error}")
                await err.channel_error('500', channel, user)
                raise Exception(errors.timeout_error)
            if not self.quiet:
                print(".", end="", flush=True)
            response = self.session.get(polling_url)
            if response.status_code != 200:
                if self.debug_file:
                    self.debug(f"ERROR: {errors.no_results_error}")
                await err.channel_error('900', channel, user)
                raise Exception(errors.no_results_error)
            if not response.text or response.text.find("errorMessage") != -1:
                time.sleep(1)
                continue
            else:
                break

        image_links = regex.findall(r'src="([^"]+)"', response.text)

        normal_image_links = [link.split("?w=")[0] for link in image_links]

        normal_image_links = list(set(normal_image_links))


        bad_images = [
            "https://r.bing.com/rp/in-2zU3AJUdkgFe7ZKv19yPBHVs.png",
            "https://r.bing.com/rp/TX9QuO3WzcCJz1uaaSwQAz39Kb0.jpg",
        ]
        for img in normal_image_links:
            if img in bad_images:
                await err.channel_error('1100', channel, user)
                raise Exception("Bad images")

        if not normal_image_links:
            await err.channel_error('1200', channel, user)
            raise Exception(errors.no_images_error)

        return normal_image_links