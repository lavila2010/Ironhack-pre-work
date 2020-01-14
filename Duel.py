print("-------Duel first part---------")
def main():
    gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
    saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

    victory_record_gandalf = [] #assign 0 Assign 0 to each variable that stores the victories
    victory_record_saruman = []

    def gandalf_win (score):
        print("Round:", score, ":", "Gandalf wins.")
        victory_record_gandalf.append(0)

    def saruman_win (score):
        print("Round:", score, ":", "Saruman wins")
        victory_record_saruman.append(0)

    def total_win(victory_record_gandalf,  victory_record_saruman):
        print(" ")
        if len(victory_record_saruman) > len(victory_record_gandalf):
            print("Match Result: Saruman won the match.")
        elif len(victory_record_gandalf) > len(victory_record_saruman):
            print("Match Result: Gandalf won the match.")
        else:
            print("Match Result: Tie.")


    for score in range(len(gandalf)):
        if gandalf[score] > saruman[score]:
            gandalf_win(score)
        elif gandalf[score] < saruman[score]:
            saruman_win(score)
        else:
            print("Raund:",score,":","Tie.")

    total_win(victory_record_gandalf,victory_record_saruman)

if __name__ == '__main__':
    main()

print("---------Duel Bonus part----------")
import statistics as stats


def gandalf_win(score):
    print("Round:", score, ":", "Gandalf wins.")
    # victory_record_gandalf.append(0)

def saruman_win (score):
    print("Round:", score, ":", "Saruman wins")
    #victory_record_saruman.append(0)
def show_stats(gandalf_wins,saruman_wins,gandalf_spells,saruman_spells):
    print("Gandalf wins the match. ")
    # total_win(gandalf_wins, saruman_wins)
    print("Gandalf wins=", gandalf_wins)
    print("Saruman wins =", saruman_wins)
    average_gandalf_spell = sum(gandalf_spells) / len(gandalf_spells)
    print("Average Gandalf spells:", average_gandalf_spell)
    average_saruman_spell = sum(saruman_spells) / len(saruman_spells)
    print("Average Saruman spells:", average_saruman_spell)

    std_gandalf_spells = (stats.stdev(gandalf_spells))
    print("Gandalfs Spell standard deviation:%.2f" % std_gandalf_spells)
    std_Saruman_spells = (stats.stdev(saruman_spells))
    print("Saruman Spell standard deviation:%.2f" % std_Saruman_spells)


def main():
    POWER = {
    'Fireball': 50,
    'Lightning bolt': 40,
    'Magic arrow': 10,
    'Black Tentacles': 25,
    'Contagion': 45
}
    gandalf_spells=[]
    saruman_spells=[]

    gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball',
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
    saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles',
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

    for i in gandalf:
        gandalf_spells.append(int(POWER[i]))
    for i in saruman:
        saruman_spells.append(int(POWER[i]))

    gandalf_wins = 0
    saruman_wins = 0
    tie_rounds=0


#Define two counter for saruman and gandlaf
#increment them by each win (limit 3)




    for score in range(len(gandalf)):
        if gandalf_spells[score] > saruman_spells[score]: #Gandalf win round
            gandalf_wins += 1
            saruman_wins = 0
            if gandalf_wins == 3:
                show_stats(gandalf_wins, saruman_wins, gandalf_spells, saruman_spells)
                exit()
        elif gandalf_spells[score] < saruman_spells[score]: # Saruman win round
            saruman_wins += 1
            gandalf_win = 0
            if saruman_wins == 3:
                show_stats(gandalf_wins, saruman_wins, gandalf_spells, saruman_spells)
                exit()

        else:
            print("Round ties:",score)

    show_stats(gandalf_wins, saruman_wins, gandalf_spells, saruman_spells)

if __name__ == '__main__':
    main()

