from django.apps import apps

from AppQatarWC2022.stickers import PlayerSticker,PlayerPosition,GeneratedSticker
from AppQatarWC2022.promo_codes import PromoCode
from AppQatarWC2022.users import UserProfile
from AppQatarWC2022.countries import Country
from AppQatarWC2022.album import Album,AlbumPage
from assertions import InstanceCreationFailed, SystemRestrictionInfringed, DataInconsistencyFound
from AppQatarWC2022.article import Article

app = apps.get_app_config('AppQatarWC2022')