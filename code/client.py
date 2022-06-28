try:
    import grpc
    import calculator_pb2       # gRPC file generated
    import calculator_pb2_grpc  # gRPC file generated
except Exception as e:
    print("Error Loading Modules!")

# Step 1: Create Channel
channel = grpc.insecure_channel('localhost:80')

# Step 2: Create Stub
stub = calculator_pb2_grpc.CalculatorStub(channel)

# Step 3: Call API
number = calculator_pb2.Number(value=20)
response = stub.SquareRoot(number)
print(response.value)