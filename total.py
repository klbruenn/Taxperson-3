import item

def total(anItem):
    """
    This method calculates the tax on 
    item.Item prices of more than 0 cent.
    """

    if anItem.price <= 0:
        raise ValueError("total does not compute prices at or below 0 cent")

    if anItem.necessary:
        tax = anItem.price * 0.01
    else:
        tax = anItem.price * 0.09
    return anItem.price + tax

