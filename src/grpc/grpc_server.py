import grpc
from concurrent import futures
import library_pb2
import library_pb2_grpc

class LibraryServicesServices(library_pb2_grpc.LibraryServiceServicer):
    def sendbook_authors(self , requerst , context):
        for book in requerst.book:
            print(f'Recive {book.title} by book {book.author.first_name} , {book.author.last_name}')
            return library_pb2
        

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    library_pb2_grpc.add_LibraryServiceServicer_to_server(LibraryServicesServices() , server)
    server.add_insecure_port('0.0.0.0:50051')
    server.wait_for_termination()


if __name__ == '__main__':
    server()
