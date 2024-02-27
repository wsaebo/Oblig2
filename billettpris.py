

def billettpris():
  print("Skriv alder på kjøperen")
  alder=input(int)
  billettpris=0
  if alder <=17:
    billettpris=30 
  elif alder >17&alder<=67:
    bilettpris=50
  else:
    billettpris=35

    print("Billettprisen er ", billettpris)



billettpris()


    
    
