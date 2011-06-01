
# TemplaTex: a generator LaTeX templates.
# Copyright (C) 2011 Rosa Durante <rosunix@gmail.com>
#                    Noelia Sales <noelia.salesmontes@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Create your views here.

import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext
from django.template.loader import render_to_string

from latex.forms import BasicDocument, Article
from latex.utils import get_basic_datas, get_article_datas


def index(request):
    if request.method == 'POST':
        form = BasicDocument(request.POST)
        if form.is_valid():
            # Aqui tendria que enviar los datos basicos.
            contents = get_basic_datas(form)
            return HttpResponseRedirect(contents[0] + '/')
    else:
        form = BasicDocument()

    return render_to_response('latex/index.html', {
            'action': '/latex/',
            'form': form,
            }, context_instance=RequestContext(request))


def article(request):
    if request.method == 'POST':
        form = Article(request.POST)
        if form.is_valid():
            # Aqui tendria que enviar los datos del articulo.
            datas = get_article_datas(form)
            file_name = datas['file_name'] or 'article.tex'

            rstring = render_to_string('latex/article.tex', datas,
                                       context_instance=RequestContext(request))
            response = HttpResponse(mimetype='application/x-latex')
            response['Content-Disposition'] = 'attachment;filename="%s"' % file_name
            response.write(rstring)
            return response
    else:
        form = Article()

    return render_to_response('latex/index.html', {
            'action': '/latex/article/',
            'form': form,
            }, RequestContext(request))
