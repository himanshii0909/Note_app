from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


@api_view(['GET', 'POST'])
def get_notes(request):

    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# ✅ NEW DELETE FUNCTION
@api_view(['DELETE'])
def delete_note(request, id):
    try:
        note = Note.objects.get(id=id)
        note.delete()
        return Response({"message": "Deleted successfully"})
    except Note.DoesNotExist:
        return Response({"error": "Note not found"})