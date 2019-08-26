# Django Feather

A simple Tag (`{% icon "name" %}`) to implement [Feather Icons](https://feathericons.com) in Django.

## Install
Install `django-feather` using `pip` and put it into your `INSTALLED_APPS`:
```bash
pip install django-feather
```  
`settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'django_feather',
    # ...
]
```

## Usage
After installation, the tag can be used just like any other tag:

```djangotemplate
{% load icon %}

<p>Using a string {% icon "coffee" class="css-class" height="8" width="8" %}</p>
<p>Using a variable {% icon self.icon class="css-class" height="8" width="8" %}</p>

```

The `icon` tag will simply take the SVG source from the Feather project,
apply additional attributes and return the SVG tag.

## Performance
`django-feather` does not read the `.svg` files each time an icon is rendered.
Instead, all the icons are written to a `.py` file upon build, just like the JavaScript
library.  
However, other than the JavaScript library, icons are rendered on the server side.
This avoids having to call `feather.replace()` after the page has loaded.  

## License
Feather is licensed under the [MIT License](https://github.com/colebemis/feather/blob/master/LICENSE).
    
`django-feather` is licensed under the Apache License, Version 2.0:

    Copyright 2019 Jonas Drotleff <j.drotleff@desk-lab.de>
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
