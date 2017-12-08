from __future__ import division
from classes import Database

class Stat_rating:

    def __init__(self):
        return

    def stat_percent(self, stat, average, accuracy = 100):

        #print int(round(stat*accuracy/(average)))
        return (round(stat*accuracy/(average),3))

    def damage_type_rating(self, physical, magic, true, total):

        accuracy=100
        ratio_p = physical / total
        ratio_m = magic / total
        ratio_t = true / total
        return [int(round(ratio_p*accuracy)), int(round(ratio_m*accuracy)), int(round(ratio_t*accuracy))]

    def rank_mapping(self, rank):
        result =1000
        if rank == "UNRANKED":
            result = 0
        if rank == "BRONZE":
            result = 1
        if rank == "SILVER":
            result = 2
        if rank == "GOLD":
            result = 3
        if rank == "PLATINUM":
            result = 4
        if rank == "DIAMOND":
            result = 5
        if rank == "MASTER":
            result = 6
        if rank == "CHALLENGER":
            result = 7
        return result

