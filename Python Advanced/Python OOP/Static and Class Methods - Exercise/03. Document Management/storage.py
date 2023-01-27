from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = [c for c in self.categories if c.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = [t for t in self.topics if t.id == topic_id][0]
        topic.storage_folder = new_storage_folder
        topic.topic = new_topic

    def edit_document(self, document_id: int, new_file_name: str):
        doc = [d for d in self.documents if d.id == document_id][0]
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(topic)

    def delete_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(doc)

    def get_document(self, document_id):
        doc = [d for d in self.documents if d.id == document_id][0]
        return doc

    def __repr__(self):
        result = [*[str(el) for el in self.documents]]
        return '\n'.join(result)




