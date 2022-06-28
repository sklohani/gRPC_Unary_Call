try:
    import grpc
    from concurrent import futures
    import time
    import calculator
    import calculator_pb2       # gRPC file generated
    import calculator_pb2_grpc  # gRPC file generated
except Exception as e:
    print("Error Loading Modules!")

ONE_DAY_IN_SECS = 60*60*24

class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    print("Starting Server. Listening on port 80.")
    server.add_insecure_port('[::]:80')
    server.start()

    try:
        while True:
            time.sleep(ONE_DAY_IN_SECS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run()