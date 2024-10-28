#Mark White
#CSD325
#Assignment 1.3

#This program will ask for the number of bottled beers
#will then sing the bottles of beer song
def main():
    bottles = int(input("How many bottles of beer on the wall? "))
    print("\n")
    while bottles > 1:
      new_bottles= bottles - 1
  
      print(bottles, "bottles of beer on the wall,", bottles , "bottles of beer.")
      print("Take one down, pass it around,", new_bottles,
            "bottle(s) of beer on the wall.")
      print("\n")
      bottles = new_bottles
  
      if bottles == 1:
        new_bottles = bottles - 1
        print(bottles, "bottle of beer on the wall,",bottles , "bottle of beer.")
      
        print("Take one down, pass it around", new_bottles, 
              "bottles of beer on the wall. \n")
    else:
          print("No more bottles of beer on the wall. Time to buy more!")
          return
main()
