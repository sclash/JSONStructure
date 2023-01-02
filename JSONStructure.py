
PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

def unlist_dict(d: dict, sep = '  '):
    s = []
    for k, _ in d.items():
        if type(d[k]) is not dict:
            s.append(f"{sep}{TEE}{k} type: {type(d[k])}")
        else:
            s.append(f"\n{sep}{TEE}  {k}")
            s.append(unlist_dict(d[k], sep = f"  {sep}"))
    return '\n'.join(s)