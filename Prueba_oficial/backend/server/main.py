import grpc
import myproto_pb2
import myproto_pb2_grpc
from credentials import database_auth
from concurrent import futures


class DataServer(myproto_pb2_grpc.Data):
    

    def GetWeatherData(self, request, context):
        print("GetWeatherData")
        #extract the more refrehing time of the db
        cur.execute("SELECT * FROM weather order by id desc limit 1")
        weather = cur.fetchall()
        temperature = {
            "id": int(weather[0][0]),
            "temp": str(weather[0][1]),
        }
        temperature_response = myproto_pb2.WeatherResponse(**temperature)
        return temperature_response
    

    def GetCoinsData(self, request, context):
        print("GetCoinsData")
        cur.execute("SELECT * FROM cash order by id desc limit 1")
        coins = cur.fetchall()
        coins = {
            "id": int(coins[0][0]),
            "dolar": str(coins[0][1]),
        }
        coins_response = myproto_pb2.CoinsResponse(**coins)
        return coins_response



    def GetUfData(self, request, context):
        print("GetUfData")
        cur.execute("SELECT * FROM uf order by id desc limit 1")
        uf = cur.fetchall()
        uf = {
            "id": int(uf[0][0]),
            "uf": str(uf[0][1]),
        }
        uf_response = myproto_pb2.UfResponse(**uf)
        return uf_response

        

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myproto_pb2_grpc.add_DataServicer_to_server(DataServer(), server)
    #Exponer a cualquier IP en el puerto 50051
    server.add_insecure_port('[::]:50051')
    server.start()
    
    print("GRPC persistor server working")
    server.wait_for_termination()


if __name__ == '__main__':
    conn = database_auth.get_db()
    cur = conn.cursor()
    main()