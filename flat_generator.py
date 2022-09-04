from logger import logger


@logger('log.txt')
def flat_generator(gen_list):

    for list_ in gen_list:

        if isinstance(list_, list):
            for item in list_:
                yield item
        else:
            yield list_
