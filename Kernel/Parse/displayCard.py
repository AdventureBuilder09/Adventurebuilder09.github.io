# ternary expression re:
# \(([^\?]+) \? ([^:]+) \: (.*)\)
# (\2 if \1 else \3)

# .length re
# ([^\( ]+?)\.length\(
# len(\1

def width(card):
    return max(
        len(card.get("name")) + len(card.get("mana_cost")) + 5, # min 5 spaces
        len(card.get("type_line")),
        len(" Edhrec rank: ") + len(str(card.get("edhrec_rank"))) + 
            (0 if card.get("power") == None else len(card.get("power")) + len(card.get("toughness")) + 6 if card.get("loyalty") == None else len(card.get("loyalty")) + 4)
        )
    


def card(card, minw = 0):
    cardwidth = max(minw, width(card))
    singleDiv = "╟" + repeat("─", cardwidth) + "╢\n"
    spaceDiv  = "║" + repeat(" ", cardwidth) + "║\n"

    ret = "╔" + repeat("═", cardwidth) + "╗\n"
    ret += "║" + card.get("name") + repeat(" ", cardwidth - len(card.get("name")) - len(card.get("mana_cost")))
    ret += card.get("mana_cost") + "║\n" + singleDiv + spaceDiv + spaceDiv + singleDiv
    ret += "║" + card.get("type_line") + repeat(" ", cardwidth - len(card.get("type_line"))) + "║\n"
    ret += singleDiv
    for line in card.get("oracle_text").split("\n"):
        ret += wrap(line, cardwidth+1)
        ret += wrap(" ",cardwidth+1)
    lastline = "║ " + "Edhrec rank: " + str(card.get("edhrec_rank"))
    if "power" in card.keys():
        lastline += " | " + repeat(" ", cardwidth -
               len(card.get("power")) - len(card.get("toughness")) -
               len(lastline) - 5)
        lastline += " " + card.get("power") + "/" + card.get("toughness") + " ║\n"
    
    elif ("loyalty") in card.keys():
        lastline += " | " + repeat(" ", cardwidth -
               len(card.get("loyalty")) - len(lastline) - 1)
        ret += card.get("loyalty") + " ║\n"
    else:
        lastline += repeat(" ", cardwidth - len(lastline)) + " ║\n"
    ret += singleDiv
    ret += lastline
    ret += "╚"+repeat("═", cardwidth)+"╝"
    return ret

def repeat(string, num):
#    if num<0:
#        print("Attempting to repeat ",string," ", num, " times")
    ret = ""
    for i in range(num):
        ret += string
    return ret

def wrap(line, lineLength):
    
        if (len(line) == 0):
            return "║" + repeat(" ", lineLength-1) + "║\n"
        if (len(line) <= lineLength):
            return "║" + line + repeat(" ", lineLength - len(line) - 1) + "║\n"

        words = line.split(" ")
        allLines = ""
        trimmedLine = "║"
        for word in words:
            if (len(trimmedLine) + 1 + len(word) <= lineLength):
                trimmedLine += (word) + (" ")
            else:
                trimmedLine += repeat(" ", lineLength - len(trimmedLine))
                allLines += (trimmedLine) + ("║\n")
                trimmedLine = "║"
                trimmedLine += (word) + (" ")
        if (len(trimmedLine) > 0):
            trimmedLine += repeat(" ", lineLength - len(trimmedLine))
            allLines += (trimmedLine)
        
        allLines += ("║\n")
        return allLines


def grid(cards, numCards, numCardsPerLine, minwid):
        numPrinted = 0;
        ret = "";
        while(numPrinted < numCards and numPrinted < len(cards)):
            row = []
            for cnum in range(numCardsPerLine):
                if numPrinted == numCards:
                    break
                row.append(card(cards[numPrinted], minwid).split("\n"))
                numPrinted += 1
            curstrow = 0
            while (True):
                nextrow = ""
                hasrow = False
                for cstr in row:
                    if (curstrow < len(cstr)):
                        hasrow = True
                if hasrow == False:
                    break
                
                for cstr in row:
                    if (curstrow < len(cstr)):
                        nextrow += cstr[curstrow] + " "
                    else:
                        nextrow += repeat(" ", len(cstr[0])+1)
                ret += nextrow + "\n"
                curstrow += 1
            ret += "\n"
        if numPrinted >= len(cards):
            ret += "========= End of Results =========\n"
        return ret
    
def listM(cards, numCards, width):
        numPrinted = 0;
        ret = "";
        while(numPrinted < numCards and numPrinted < len(cards)):
            ret += cards[numPrinted].get('name') + repeat(" ", width-len(cards[numPrinted].get('name'))-len(cards[numPrinted].get('mana_cost'))) + cards[numPrinted].get('mana_cost') + "\n"
            numPrinted += 1
        if numPrinted >= len(cards):
            ret += "========= End of Results =========\n"
        return ret
    
def listT(cards, numCards, width):
        numPrinted = 0;
        ret = "";
        while(numPrinted < numCards and numPrinted < len(cards)):
            ret += cards[numPrinted].get('name') + repeat(" ", width-len(cards[numPrinted].get('name'))-len(cards[numPrinted].get('type'))) + cards[numPrinted].get('type') + "\n"
            numPrinted += 1
        if numPrinted >= len(cards):
            ret += "========= End of Results =========\n"
        return ret
    
def listPT(cards, numCards, width):
        numPrinted = 0;
        ret = "";
        while(numPrinted < numCards and numPrinted < len(cards)):
            ret += cards[numPrinted].get('name')
            if 'power' in cards[numPrinted]:
                ret += repeat(" ", width-len(cards[numPrinted].get('name'))-len(cards[numPrinted].get('power'))-len(cards[numPrinted].get('toughness'))-1) + cards[numPrinted].get('power') + "/" + cards[numPrinted].get('toughness') + "\n"
            numPrinted += 1
        if numPrinted >= len(cards):
            ret += "========= End of Results =========\n"
        return ret
