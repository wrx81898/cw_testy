Instrukcja użycia:

Upewnij się, że masz zainstalowaną bibliotekę requests oraz json.

Uruchom skrypt:

bash

    python test_endpoints.py

Opis skryptu:

Funkcja check_response wysyła żądanie GET do podanego URL za pomocą requests.get(), sprawdza kod odpowiedzi HTTP i jeśli jest to 200, przekazuje ciało odpowiedzi do funkcji check_json.
Funkcja check_json sprawdza obecność kluczowych elementów (id, title) w odpowiedzi JSON.
Skrypt iteruje przez listę endpointów, testując każdy z nich i wyświetlając wyniki w czytelny sposób.

Użycie Makefile:

Aby zainstalować zależności, uruchom:

    make install

Aby uruchomić aplikację, uruchom:

    make run

Aby przetestować aplikację, uruchom:

    make test