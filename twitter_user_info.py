import twitter1
import twitter2

param_dict = {}


def recursion_twi(dic):
    """
    dict -> None
    Recursive processing of python dict from json file and rewriting
    into param_dict.
    """
    global param_dict
    for i in dic:
        if type(dic[i]) == dict:
            recursion_twi(dic[i])
        elif dic[i] and i not in param_dict:
            param_dict[i] = dic[i]


def ask(param_dict):
    """
    list or dict -> dict
    Return rewritten dict with all user key-information.
    """
    while True:
        a = input('Choose one key: ' + ' ,'.join(param_dict.keys()) + '\n')
        if len(a) < 1:
            break
        elif a not in param_dict:
            print('Wrong input!')
        else:
            print(param_dict.get(a))


def main():
    """
    Get information about any twitter-user.
    """
    while True:
        global param_dict
        acct = input('Enter Twitter Name: ')
        lst = twitter1.twitter_info(acct)
        lst.append(twitter2.twitter_info_prof(acct))
        for i in lst:
            recursion_twi(i)
        ask(param_dict)


main()
