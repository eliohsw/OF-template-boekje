from pygments.style import Style
from pygments.token import Comment, Keyword, Name, String, Error, Generic, Number, Operator, Literal, Punctuation, Text, Whitespace, Escape, Other

class style1(Style):
    """
    (2025/01/05) v1.0
    Default style for style1. Based on the lowkey style in Xcode editor.
    """
    name = 'style1'

    styles = {
        Text:                          '',
        Whitespace:                    '#BABABA',
        Escape:                        '',
        Error:                         'border:#FF0000',
        Other:                         '#000000',

        Keyword:                       'bold #262C6A',
        Keyword.Constant:              '',
        Keyword.Declaration:           '',
        Keyword.Namespace:             '',
        Keyword.Pseudo:                '',
        Keyword.Reserved:              '',
        Keyword.Type:                  '',

        Name:                          '#476A97',
        Name.Attribute:                '',
        Name.Builtin:                  '#0B4F79',
        Name.Builtin.Pseudo:           '#0B4F79',
        Name.Class:                    'bold #0B4F79',
        Name.Constant:                 '#101010',
        Name.Decorator:                '',
        Name.Entity:                   '',
        Name.Exception:                '',
        Name.Function:                 '#0F68A0',
        Name.Function.Magic:           '#0F68A0',
        Name.Property:                 '',
        Name.Label:                    '#0B4F79',
        Name.Namespace:                '#0B4F79',
        Name.Other:                    '',
        Name.Tag:                      'bold #0B4F79',
        Name.Variable:                 '',
        Name.Variable.Class:           '',
        Name.Variable.Global:          '',
        Name.Variable.Instance:        '',
        Name.Variable.Magic:           '',

        Literal:                       '',
        Literal.Date:                  '#262C6A',

        String:                        '#483356',
        String.Affix:                  '',
        String.Backtick:               '',
        String.Char:                   '#262C6A',
        String.Delimiter:              '',
        String.Doc:                    '#4A5560',
        String.Double:                 '',
        String.Escape:                 '',
        String.Heredoc:                '',
        String.Interpol:               '',
        String.Other:                  '',
        String.Regex:                  '',
        String.Single:                 '',
        String.Symbol:                 '',

        Number:                        '#262C6A',
        Number.Bin:                    '',
        Number.Float:                  '',
        Number.Hex:                    '',
        Number.Integer:                '',
        Number.Integer.Long:           '',
        Number.Oct:                    '',

        Operator:                      '#000000',
        Operator.Word:                 '#595959',

        Punctuation:                   '#000000',
        Punctuation.Marker:            '',

        Comment:                       '#4A5560',
        Comment.Hashbang:              '#232323',
        Comment.Multiline:             'italic',
        Comment.Preproc:               '#232323',
        Comment.PreprocFile:           '#483356',
        Comment.Single:                'italic',
        Comment.Special:               'italic',

        Generic:                       '',
        Generic.Deleted:               '#C4554D',
        Generic.Emph:                  '',
        Generic.Error:                 '',
        Generic.Heading:               'bold #343434',
        Generic.Inserted:              '#548164',
        Generic.Output:                '',
        Generic.Prompt:                '',
        Generic.Strong:                '',
        Generic.Subheading:            '#343434',
        Generic.EmphStrong:            '',
        Generic.Traceback:             '',
    }

class style2(Style):
    name = 'style2'