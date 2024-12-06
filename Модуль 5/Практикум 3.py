import itertools
def generate_card_deck():
    suits = ['♠', '♥', '♦', '♣']
    court_cards = ['King', 'Queen', 'Jack', 'Ace']
    num_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
    gen_court_cards = itertools.product(suits, court_cards)
    gen_num_cards = itertools.product(suits, num_cards)
    card_deck = itertools.chain(gen_court_cards, gen_num_cards)
    return [''.join(card) for card in card_deck]

def generate_combination(deck, quant):
    return itertools.combinations(deck, quant)

def save_data(combinations):
    with open('combinations.txt', 'w', encoding='utf-8') as file:
        file.write(f"\n--- Новый набор карт ---\n")
        for combination in combinations:
            file.write(str(combination) + '\n')

deck = generate_card_deck()
quant_cards = int(input('Введите количество карт в комбинации (от 1 до 52): '))
if not (1 <= quant_cards <= 52):
    print('Количество карт должно быть от 1 до 52.')
else:
    combination = list(generate_combination(deck, quant_cards))
    print(combination)

save_data(combination)