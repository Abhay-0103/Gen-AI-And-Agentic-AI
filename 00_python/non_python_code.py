def make_chai():
    if not kettele_has_water():
        fill_kettle_with_water()
    plug_in_kettle()
    boil_water()
    if not is_cup_clen():
        wash_cup()
        add_to_cup("tea bag")
        add_to_cup("sugar")
        pour("boiled water", "cup")
        stiler("cup")
        serve("chai")


make_chai()