from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import Cursos_Form, Materia_Form
from .models import Materia

@login_required
def inicio_cursos(request):
	current_user = request.user
	form = Cursos_Form(request.POST or None)

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('home_d')) #cambiarlo a lista

	#instance = get_object_or_404(Docente, id_perfil_id = current_user.id)


	context = {

		"nom": current_user.first_name,
		"ape":current_user.last_name,
		"id_d": current_user.id,
	}
	
	return render(request,"inicio_cursos.html",context)

@login_required
def materias(request,curso_id):
	current_user = request.user
	form = Materia_Form(request.POST or None)
	materia = Materia.objects.all()

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(reverse('home_d'))  #cambiarlo a lista

	context = {

		"id_d": current_user.id,
		"curso_id": int(curso_id),
		"materia":materia,
		
	}
	
	return render(request,"inicio_materias.html",context)
