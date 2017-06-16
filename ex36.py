def stone_paper_scissors(ours, theirs):
        if theirs != "stone" and theirs != "paper" and theirs != "scissors":
                print "%s is not a valid option" % theirs
                return "retry"

        if ours == theirs:
                print "%s doesn't beat %s" % (ours, theirs)
                return "retry"

        if ours == "stone" and theirs == "paper":
                print "stone doesn't beat paper"
                return "win"
        elif ours == "paper" and theirs == "scissors":
                print "paper doesn't beat scissors"
                return "win"
        elif ours == "scissors" and theirs == "stone":
                print "scissors doesn't beat stone"
                return "win"
        else:
                print "%s beats %s" % (ours, theirs)
                return "loose"


def choose_red_pill():
        print "You chose the red pill"
        outcome = "retry"
        while outcome == "retry":
                choice = raw_input("Now choose stone, paper or scissors :")
                outcome = stone_paper_scissors("paper", choice)

        if "win" == outcome:
                print "You are the one"
        else:
                print "Hello Mr. Smith"

def choose_blue_pill():
        print "You chose the blue pill"
        print "Now you wait for eternity"
        for i in range(0, 3):
                choice = raw_input("There are two doors 1 and 2 open either :")

                if choice != "1" and choice != "2":
                        print "Wrong answer eat the blue pill again scumbag"
                        choose_blue_pill()
                else:
                        if i == 2:
                                print "Eternity ends"
                        else:
                                print "You're back to where you started"

blue_pill = ['blue', 'blue pill', "blue one"]
red_pill = ['red', 'red pill', 'red one']

choice = raw_input("Choose either the red pill or the blue pill :")
if choice in blue_pill:
        choose_blue_pill()
elif choice in red_pill:
        choose_red_pill()
else:
        print "Wrong answer scumbag"
