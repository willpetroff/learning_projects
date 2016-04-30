def fast_knap_max_vol(item_wght,item_vol,item_val,avail_wght,avail_vol,index,call_back):
    try: return call_back[(index,avail_wght,avail_vol)]
    except KeyError:
        if index==0:
            if item_wght[index]<=avail_wght and item_vol[index]<=avail_vol:
                call_back[(index,avail_wght,avail_vol)]=item_val[index]
                return item_val[index]
            else:
                call_back[(index,avail_wght,avail_vol)]=0
                return 0
        else:
            without_item=fast_knap_max_vol(item_wght,item_vol,item_val,avail_wght,avail_vol,index-1,call_back)
            if item_wght[index]>avail_wght or item_vol[index]>avail_vol:
                call_back[(index,avail_wght,avail_vol)]=without_item
                return without_item
            else:
                with_item=item_val[index]+fast_knap_max_vol(item_wght,item_vol,item_val,avail_wght-item_wght[index],avail_vol-item_vol[index],index-1,call_back)
            resolution=max(with_item,without_item)
            call_back[(index,avail_wght,avail_vol)]=resolution
            return resolution

def call_fkmv(item_wght,item_vol,item_val,avail_wght,avail_vol,index):
    knap_memo={}
    return fast_knap_max_vol(item_wght,item_vol,item_val,avail_wght,avail_vol,index,knap_memo)

def main():
    item_wght=[3,6,4,7]
    item_vol=[3,7,5,4]
    item_val=[4,6,7,1]
    avail_wght=10
    avail_vol=12
    index=len(item_wght)-1
    print(call_fkmv(item_wght,item_vol,item_val,avail_wght,avail_vol,index))
