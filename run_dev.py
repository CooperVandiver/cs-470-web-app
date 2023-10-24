from subprocess import run
from app import app
from multiprocessing import Process

def run_tailwind():
    run(
        "npx tailwindcss -i app/static/css/input.css -o app/static/css/output.css --watch".split(' '),
        shell=True
    )

def main():
    p = Process(target=run_tailwind)
    p.start()
    app.run(debug=True)
    p.join()

if __name__ == '__main__':
    main()
