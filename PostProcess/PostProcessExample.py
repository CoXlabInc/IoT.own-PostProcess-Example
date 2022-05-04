import argparse
import pyiotown.post

def post_process(message):
  print(message)

  # Do something with message['data'].
  
  return message

if __name__ == '__main__':
  app_desc = 'IoT.own Post Process Example'

  parser = argparse.ArgumentParser(description=app_desc)
  parser.add_argument("--url", help="IoT.own URL", required=True)
  parser.add_argument("--user", help="IoT.own user account", required=True)
  parser.add_argument("--token", help="IoT.own API Token", required=True)
  args = parser.parse_args()

  print(app_desc)
  print(f"URL: {args.url}")

  pyiotown.post.postprocess(args.url, 'PostProcessName', post_process, args.user, args.token)
  
