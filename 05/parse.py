from typing import List, Tuple, Set
from dataclasses import dataclass
from functools import reduce


def ranges_intersect(x1, x2, y1, y2):
    return (
        (x1 >= y1 and x1 <= y2)
        or (x2 >= y1 and x2 <= y2)
        or (y1 >= x1 and y1 <= x2)
        or (y2 >= x1 and y2 <= x2)
    )


@dataclass
class RangeSet:
    ranges: Set[Tuple[int, int]]

    def remove_range(self, remove_start: int, remove_end: int):
        new_ranges = set()
        for range_start, range_end in self.ranges:
            if not ranges_intersect(range_start, range_end, remove_start, remove_end):
                new_ranges.add((range_start, range_end))
                continue
            # could either reduce the size of a range of split a range into 2
            if range_start < remove_start:
                new_ranges.add((range_start, remove_start - 1))
            if range_end > remove_end:
                new_ranges.add((remove_end + 1, range_end))
        self.ranges = new_ranges

    def get_ranges(self):
        return self.ranges


class RangeMapper:
    def __init__(self) -> None:
        self.ranges = []

    def add_range(self, destination_start, source_start, range_size) -> None:
        self.ranges.append((destination_start, source_start, range_size))

    def convert_to_destination(self, item_id: int):
        for destination_start, source_start, range_size in self.ranges:
            if item_id < source_start + range_size and item_id >= source_start:
                return item_id + destination_start - source_start
        return item_id

    def get_ranges(self):
        return self.ranges

    def convert_ranges_to_destination_ranges(
        self, input_ranges: RangeSet, debug=False
    ) -> RangeSet:
        """
        Returns a tuple of lists, where the first element is the new processed ranges,
        and the second element is the leftover item_ids in the original range
        """
        new_rangeset = set()
        for start_id, end_id in input_ranges.get_ranges():
            for destination_start, source_start, range_size in self.ranges:
                range_end_inclusive = source_start + range_size - 1
                if ranges_intersect(
                    start_id, end_id, source_start, range_end_inclusive
                ):
                    first_matching_id = max(start_id, source_start)
                    last_matching_id = min(end_id, range_end_inclusive)
                    new_rangeset.add(
                        (
                            first_matching_id - source_start + destination_start,
                            last_matching_id - source_start + destination_start,
                        )
                    )
                    input_ranges.remove_range(first_matching_id, last_matching_id)
        return RangeSet((new_rangeset | input_ranges.ranges))


@dataclass
class PlantConverter:
    seeds: List[int]
    seed_to_soil: RangeMapper
    soil_to_fertilizer: RangeMapper
    fertilizer_to_water: RangeMapper
    water_to_light: RangeMapper
    light_to_temp: RangeMapper
    temp_to_humidity: RangeMapper
    humidity_to_location: RangeMapper

    def follow_lifecycle_to_location(self, seed_num) -> int:
        result = seed_num
        result = self.seed_to_soil.convert_to_destination(result)
        result = self.soil_to_fertilizer.convert_to_destination(result)
        result = self.fertilizer_to_water.convert_to_destination(result)
        result = self.water_to_light.convert_to_destination(result)
        result = self.light_to_temp.convert_to_destination(result)
        result = self.temp_to_humidity.convert_to_destination(result)
        result = self.humidity_to_location.convert_to_destination(result)
        return result

    def follow_lifecycle_to_location_range(self, seed_range: RangeSet) -> RangeSet:
        result = seed_range
        result = self.seed_to_soil.convert_ranges_to_destination_ranges(result)
        result = self.soil_to_fertilizer.convert_ranges_to_destination_ranges(result)
        result = self.fertilizer_to_water.convert_ranges_to_destination_ranges(result)
        result = self.water_to_light.convert_ranges_to_destination_ranges(result)
        result = self.light_to_temp.convert_ranges_to_destination_ranges(result)
        result = self.temp_to_humidity.convert_ranges_to_destination_ranges(result)
        result = self.humidity_to_location.convert_ranges_to_destination_ranges(result)
        return result


def parse_input(filename) -> PlantConverter:
    seeds = []
    seed_to_soil = RangeMapper()
    soil_to_fertilizer = RangeMapper()
    fertilizer_to_water = RangeMapper()
    water_to_light = RangeMapper()
    light_to_temp = RangeMapper()
    temp_to_humidity = RangeMapper()
    humidity_to_location = RangeMapper()
    lists = [
        seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temp,
        temp_to_humidity,
        humidity_to_location,
    ]
    with open(filename) as f:
        list_idx = -1
        for line in f:
            line = line.strip()
            if line.startswith("seeds:"):
                seeds = line.strip().split(":")[1].split(" ")
                seeds = list(map(int, filter(lambda x: len(x) > 0, seeds)))
            elif line.strip().endswith(":"):
                list_idx += 1
            elif len(line) == 0:
                pass
            else:
                processed_triple = tuple(
                    map(int, filter(lambda x: len(x) > 0, line.strip().split(" ")))
                )
                lists[list_idx].add_range(*processed_triple)

    return PlantConverter(seeds, *lists)
