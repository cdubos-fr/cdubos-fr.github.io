set shell := ["zsh", "-uc"]

devenv:
    pre-commit install

[working-directory: 'source']
build:
    zola build

[working-directory: 'source']
serve:
    zola serve --port 1111

[working-directory: 'source']
clean:
    rm -rf public
