from log import logger

def writeMessage():
    lines = []

    try:
        while True:
            line = input()
            lines.append(line)
    
    except KeyboardInterrupt as e:
        logger.critical(e)
        text = '\n'.join(lines)
        
        return text