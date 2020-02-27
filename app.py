from flask import Flask

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def status():
  return 'Hello World!', 200

def main():
  APP.run()

if __name__ == '__main__':
  main()