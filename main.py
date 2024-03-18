import heapq

def min_cost_to_combine_cables(cable_lengths):
    # Створюємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    while len(cable_lengths) > 1:
        # Виймаємо два кабелі з найменшою довжиною
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Об'єднуємо ці кабелі
        combined_length = first + second
        total_cost += combined_length

        # Додаємо новий кабель назад у купу
        heapq.heappush(cable_lengths, combined_length)
    
    return total_cost

# Тестуємо функцію з прикладними довжинами кабелів
test_cables = [5, 4, 2, 8]
min_cost_to_combine_cables(test_cables)
