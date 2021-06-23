import requests, sys
from sys import argv as a

style_bold = '\033[1m'
color_blue = '\033[94m'

def format_and_send_problem(problemName, displayedName, promptHtml_path, starterCode_path,                  hint_path, testCases_path, url, pwd):
    datas = [open(promptHtml_path, "r").read(), open(starterCode_path, "r").read(), open(hint_path, "r").read(), open(testCases_path, "r").read()]

    for i in range(len(datas)):
        datas[i] = datas[i].translate(str.maketrans({ "\"" : "\\\"", "\'" : "\\\'" }))

    problem_dict = {
        "problemName": problemName,
        "displayedName": displayedName,
        "promptHtml": datas[0],
        "starterCode": datas[1],
        "hint": datas[2],
        "testCases": datas[3]
    }
    res = requests.post(f"{url}?pwd={pwd}", json=problem_dict)
    return res.text


if __name__ == "__main__":
    interactive = False
    for ele in a:
        if ele == "-h" or ele == "--help":
            print(f"{style_bold}usage: python3 send_request.py <problemName> <displayedName> <promptHtml_path> \
<starterCode_path> <hint_path> <testCases_path> <url> <pwd>")
            print(f"{style_bold}interactive mode: python3 send_request.py -i|--interactive")
            print(f"{style_bold}print this help: python3 send_request.py -h|--help")
            sys.exit(0)
        if ele == "-i" or ele == "--interactive":
            interactive = True
    res_text = ""
    if interactive:
        promptList = ["Problem Name: ", "Displayed name: ", "Prompt HTML path: ", "Starter code path: ", "Hint path: ", "Test cases path: ", "Request url: ", "Request password: "]
        args = []
        for p in promptList:
            args.append(input(f"{color_blue}{p}"))
        res_text = format_and_send_problem(args[0], args[1], args[2], args[3], args[4], args[5],\
        args[6], args[7])
    else:
        res_text = format_and_send_problem(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8])
    print(res_text)
