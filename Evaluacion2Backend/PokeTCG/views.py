from django.shortcuts import render, get_object_or_404, redirect

from .models import Card, Pokemon, Element, Expansion
from .forms import CardForm, PokeForm, ElementForm, ExpanForm

# Create your views here.


#Card views
def card_list(request):
    cards = Card.objects.all()
    return render(request, 'PokeTCG/Card/card_list.html',{'cards':cards})

def card_detail(request, pk):
    card = get_object_or_404(Card,pk=pk)
    return render(request,'PokeTCG/Card/card_detail.html',{'card':card} )

def card_add(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            card.save()
            return redirect('card_detail', pk = card.pk)
    else:
        form = CardForm()
    return render(request, 'PokeTCG/Card/card_edit.html',{'form':form})

def card_delete(request,pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method=='POST':
        card.delete()
        return redirect('card_list')
    return render(request, 'PokeTCG/Card/card_detail.html',{'card':card})

def card_edit(request,pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            card=form.save(commit=False)
            card.save()
            return redirect('card_detail',pk=card.pk)
    else:
        form = CardForm(instance=card)
    return render(request, 'PokeTCG/Card/card_edit.html',{'form':form})



#Pokemon views

def poke_list(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'PokeTCG/Pokemon/poke_list.html', {'pokemons': pokemons})

def poke_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'PokeTCG/Pokemon/poke_detail.html', {'pokemon': pokemon})

def poke_add(request):
    if request.method == "POST":
        form = PokeForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.save()
            return redirect('poke_detail', pk=pokemon.pk)
    else:
        form = PokeForm()
    return render(request, 'PokeTCG/Pokemon/poke_edit.html', {'form': form}) 

def poke_delete(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        pokemon.delete()
        return redirect('poke_list')
    return render(request, 'PokeTCG/Pokemon/poke_detail.html', {'pokemon': pokemon})

def poke_edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        form = PokeForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.save()
            return redirect('poke_detail', pk=pokemon.pk)
    else:
        form = PokeForm(instance=pokemon)
    return render(request, 'PokeTCG/Pokemon/poke_edit.html', {'form': form})

#Expansion views

def expan_list(request):
    expansions = Expansion.objects.all()
    return render(request, 'PokeTCG/Expansion/expan_list.html', {'expansions': expansions})

def expan_detail(request, pk):
    expansion = get_object_or_404(Expansion, pk=pk)
    return render(request, 'PokeTCG/Expansion/expan_detail.html', {'expansion': expansion})

def expan_add(request):
    if request.method == "POST":
        form = ExpanForm(request.POST)
        if form.is_valid():
            expansion = form.save(commit=False)
            expansion.save()
            return redirect('expan_detail', pk=expansion.pk) 
    else:
        form = ExpanForm()
    return render(request, 'PokeTCG/Expansion/expan_edit.html',{'form':form})

def expan_delete(request, pk):
    expansion = get_object_or_404(Expansion, pk=pk)
    if request.method == "POST":
        expansion.delete()
        return redirect('expan_list')
    return render(request, 'PokeTCG/Expansion/expan_detail.html', {'expansion': expansion})

def expan_edit(request, pk):
    expansion = get_object_or_404(Expansion, pk=pk)
    if request.method == "POST":
        form = ExpanForm(request.POST, instance=expansion)
        if form.is_valid():
            expansion = form.save(commit=False)
            expansion.save()
            return redirect('expan_detail', pk=expansion.pk)
    else:
        form = ExpanForm(instance=expansion)
    return render(request, 'PokeTCG/Expansion/expan_edit.html', {'form': form})

#Element views


def element_list(request):
    elements = Element.objects.all()
    return render(request, 'PokeTCG/Element/element_list.html', {'elements': elements})

def element_detail(request, pk):
    element = get_object_or_404(Element, pk=pk)
    return render(request, 'PokeTCG/Element/element_detail.html', {'element': element})

def element_add(request):
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.save()
            return redirect('element_detail', pk=element.pk)
    else:
        form = ElementForm()
    return render(request, 'PokeTCG/Element/element_edit.html', {'form': form})

def element_edit(request, pk):
    element = get_object_or_404(Element, pk=pk)
    if request.method == "POST":
        form = ElementForm(request.POST, instance=element)
        if form.is_valid():
            element = form.save(commit=False)
            element.save()
            return redirect('element_detail', pk=element.pk)
    else:
        form = ElementForm(instance=element)
    return render(request, 'PokeTCG/Element/element_edit.html', {'form': form})

def element_delete(request, pk):
    element = get_object_or_404(Element, pk=pk)
    if request.method == "POST":
        element.delete()
        return redirect('element_list')
    return render(request, 'PokeTCG/Element/element_detail.html', {'element': element})
