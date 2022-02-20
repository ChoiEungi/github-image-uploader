import datetime
import json
from sys import argv

import requests
import base64


def json_default(value):
    if (isinstance(value, bytes)):
        return str(value, encoding="utf-8")


class GithubApiRequest:
    def __init__(self, image_path, owner, repository_name):
        self.image_path = image_path
        self.owner = owner
        self.repository_name = repository_name
        self.branch = "master"

    def __init__(self, image_path, owner, repository_name, branch):
        self.image_path = image_path
        self.owner = owner
        self.repository_name = repository_name
        self.branch = branch

    def get_image_url_from_response(self):
        response_json = self.github_file_upload_api_request()
        return response_json["content"]["download_url"]

    def github_file_upload_api_request(self):
        headers = self.header_request()
        body = self.body_request()
        url = self.url_request()
        response = requests.request("PUT", url, headers=headers, data=body)
        return response.json()

    def header_request(self):
        with open("token") as f:
            github_token = f.readlines()[0]

        token_header_content = "Bearer " + github_token
        headers = {"Authorization": token_header_content, "Content-Type": "application/json"}
        return headers

    def body_request(self):
        with open(self.image_path, 'rb') as img:
            encoded_image = base64.b64encode(img.read())

        body = {"message": "hello",
                "content": encoded_image,
                "branch": self.branch
                }

        return json.dumps(body, default=json_default)

    def url_request(self):
        time = datetime.datetime.now().date().__str__() + "-" + datetime.datetime.now().time().__str__()
        path = time.split(".")[0] + ".png"
        url = f"https://api.github.com/repos/{self.owner}/{self.repository_name}/contents/{path}"
        return url


if __name__ == "__main__":
    if len(argv) < 2:
        print("usage: python3 main.py {image_path}")
        exit(1)

    image_path = argv[1]
    api_request = GithubApiRequest(image_path=image_path, owner="ChoiEungi", repository_name="git-blog-image", branch="upload")
    print(api_request.get_image_url_from_response())
