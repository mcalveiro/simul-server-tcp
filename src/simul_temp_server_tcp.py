import socket
import time

# Configuración del cliente TCP
SERVER_IP = '192.168.100.2'  # Cambia a la dirección IPv4 de tu adaptador Wi-Fi
SERVER_PORT = 8090  # Asegúrate de que tu servidor esté escuchando en este puerto

# Parámetros para la fluctuación de temperatura
TEMP_MIN = 23.5  # Temperatura mínima
TEMP_MAX = 50.0  # Temperatura máxima
INTERVAL = 5  # Intervalo de 5 segundos
STEP = 0.5  # Incremento/decremento por ciclo

def main():
    # Crear el socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectar al servidor
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Conectado al servidor {SERVER_IP}:{SERVER_PORT}")
        
        temperature = TEMP_MIN
        increasing = True  # Control para la rampa

        while True:
            # Enviar el dato de temperatura al servidor
            message = f"{temperature:.2f}\n"
            client_socket.sendall(message.encode('utf-8'))
            print(f"Temperatura enviada: {message.strip()}")
            
            # Verificar si estamos subiendo o bajando la temperatura
            if increasing:
                temperature += STEP
                if temperature >= TEMP_MAX:
                    increasing = False  # Cambiar a descenso
            else:
                temperature -= STEP
                if temperature <= TEMP_MIN:
                    increasing = True  # Cambiar a ascenso

            # Esperar 5 segundos antes de enviar el próximo dato
            time.sleep(INTERVAL)
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cerrar el socket
        client_socket.close()

if __name__ == "__main__":
    main()
