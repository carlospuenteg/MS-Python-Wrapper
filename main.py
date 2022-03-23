code = open("code.txt", "r").read().split("\n")

def codeObj(code):
    codeArr = []
    for line in code:
        line = line.strip().replace("\t","").split(":")

        label = line[0].strip() if len(line) > 1 else ""
        operation = line[-1].strip().split(" ")
        operator = operation[0]
        args = [x.replace(",","").strip() for x in operation[1:]]

        lineObj = { "label": label, "operator": operator, "args": args }
        codeArr.append(lineObj)
    return codeArr

code = codeObj(code)

##########################################################################

def execute(code):
    vars = {}
    pos = {}
    isTrue = False
    index = 0

    for i,line in enumerate(code):
        if line["label"]:
            if line["operator"]=="dato":
                vars[line["label"]] = int(line["args"][0],16)
            else:
                pos[line["label"]] = i

    while True:
        line = code[index]
        if line["operator"]=="beq" and line["label"]==line["args"][0]:  # If you reach the end
            return vars

        if line["operator"]=="cmp":
            if vars[line["args"][0]] == vars[line["args"][1]]:
                isTrue = True
            else:
                isTrue = False

        elif line["operator"]=="beq":
            if isTrue:
                index = pos[line["args"][0]] - 1  # "-1" Because index gets increased after
        
        elif line["operator"]=="add":
            vars[line["args"][1]] += vars[line["args"][0]]
        
        elif line["operator"]=="mov":
            vars[line["args"][1]] = vars[line["args"][0]]

        index += 1

print( execute(code) )
