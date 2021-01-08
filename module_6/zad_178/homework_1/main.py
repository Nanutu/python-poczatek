#
# Uzupełnij szablon kodu o odpowiednie implementacje (oznaczenia TODO)
#  - Funkcje z user_interface po uruchomieniu programu zapytają użytkownika o dane (imię i nazwisko)
#  a następnie zaproponują dodanie kolejnych towarów do zamówienia.
#  - W celu kontroli dostępności towarów klasa Store, posiada zdefiniowaną listę dostępnych produktów i ich liczbę.
#  Podczas dodawania kolejnych produktów do zamówienia aktualizuj ich stan w Store i gdyby okazało się,
#  że nie można zrealizować oczekiwań klienta wyrzuć odpowiedni wyjątek i obsłuż go komunikatem dla użytkownika.

# Rozbuduj rozwiązanie zadania trzeciego z lekcji 167. PP: Wyjątki w Pythonie o utrwalanie złożonych zamówień.
#
# Przed wyłączeniem programu dopisz złożone zamówienie (wynik wykonania str na obiekcie zamówienia) do pliku orders.txt.
#
# Plik orders.txt powinien znajdować się w katalogu data - wykorzystaj ścieżkę względną by się do niego odwołać.


from shop import user_interface


def run_homework():
    user_interface.handle_customer()


if __name__ == '__main__':
    run_homework()
