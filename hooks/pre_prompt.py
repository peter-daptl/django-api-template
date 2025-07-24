import json
import os
import secrets

def generate_secret_key(length=50):
    return secrets.token_urlsafe(length)


cookie_cutter_json_path = os.path.join(os.getcwd(), "cookiecutter.json")

try:
    with open(cookie_cutter_json_path, "r") as f:
        cookiecutter_context = json.load(f)

    generated_secret_key = generate_secret_key()

    cookiecutter_context["_secret_key"] = generated_secret_key

    with open(cookie_cutter_json_path, "w") as f:
        json.dump(cookiecutter_context, f, indent=2)
    print(f"pre_prompt: Successfully injected dynamic secret_key into {cookie_cutter_json_path}")

except FileNotFoundError:
    print(f"pre_prompt: Error: cookiecutter.json not found at {cookie_cutter_json_path}.")
except json.JSONDecodeError:
    print("pre_prompt: Error: Could not decode cookiecutter.json. Is it valid JSON?")
except Exception as e:
    print(f"pre_prompt: An unexpected error occurred: {e}")
