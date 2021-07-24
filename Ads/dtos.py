from .models import Price, Discount

# price = Price.objects.filter()
class ChannelDto:
    pass

def get_dto(channels):
    listt = []
    for channel in channels:
        chn = ChannelDto()
        chn.id = channel.id
        chn.name = channel.name
        chn.image = channel.image
        chn.price = Price.objects.get(pk=channel.id).price_per_symbol
        chn.discounts = Discount.objects.filter(pk=channel.id)
        listt.append(chn)
    return listt
