from SublimeLinter.lint import Linter

class __class__(Linter):
    cmd = 'tflint ${file}'
    name = 'tflint'
    regex = r'.*(?:(?P<error>Error)|(?P<warning>(?:(Warning|Notice)))):\s(?P<message>.+)\n\n.*line\s(?P<line>\d+):'
    multiline = True
    defaults = {
        'selector': 'source.terraform'
    }
