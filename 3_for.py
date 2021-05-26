#--------------------
# Домашнее задание №1
#--------------------

# Цикл for: Оценки

#* Создать список из словарей с оценками учеников разных классов 
#  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#* Посчитать и вывести средний балл по всей школе.
#* Посчитать и вывести средний балл по каждому классу.



classes_scores = [                                       # список, содержащий словари
  {'school_class': '5a', 'scores': [3,4,4,5,2]},            # словарь, содержащий класс и оценки учеников
  {'school_class': '7b', 'scores': [5,5,3,5,4]},
  {'school_class': '8a', 'scores': [4,5,3,5,4]}, 
  {'school_class': '9a', 'scores': [5,5,5,5,5]},
  {'school_class': '9b', 'scores': [3,3,3,4,4]},

]

classes_avr_score = []                                   # создаем список, и помещаем в него значения оценок в классах

def main():                                                 # функция подсчитыввет среднюю оценку в классах и добавляет это значение в список schoolkids_avr_score
  for score in classes_scores:
      classes_avr_score.append(sum(score['scores'])/len(score['scores']))
      print(f"Средняя оценка по классу {score['school_class']}: {(sum(score['scores']) / len(score['scores']))}")

  school_avr_score = sum(classes_avr_score)/len(classes_avr_score)                # подсчет средней оценки по школе
  print(f"Средняя оценка по школе: {school_avr_score}")
  
if __name__ == "__main__":
    main()