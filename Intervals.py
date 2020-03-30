import random

QUALITIES = ["Minor", "Major", "Diminshed", "Augmented", "Perfect"]

INTERVALS = ["2nd", "3rd", "4th", "5th", "6th", "7th", "8th"]

PERFINTERVALS = [2, 3, 6]

if __name__ == "__main__":
    
    while True:

        input_ = input("Another Interval? (Y/N)")

        if input_ == "n":
            break
        else:
            indice_1 = random.randint(0, 4) #Qualities
            indice_2 = random.randint(0, 6) #Intervals
            
            # Check whether generated indices correlate to 4ths, 5ths or 8ves
            if indice_2 in PERFINTERVALS:
                indice_1 = 4 #make it a perfect interval

            if indice_2 not in PERFINTERVALS:
                indice_1 = random.randint(0, 3)

            # Generate randomly up or down
            a = random.randint(0, 1)
            if a == 0:
                Up_Down = "Up"
            else:
                Up_Down = "Down"

            # Print the answer, drawing upon arrays
            ans = QUALITIES[indice_1] + " " + INTERVALS[indice_2] + " " + Up_Down
            print(ans)