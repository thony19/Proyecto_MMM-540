% Importa la biblioteca de MATLAB RESTful API
import matlab.net.*

% Crea un servidor RESTful
server_ = matlab.net.http.server.HTTPServer;

% Define una ruta y un controlador para recibir solicitudes GET
routeGet = '/data';
server_.get(routeGet, @handleGetRequest);

% Inicia el servidor
server_.start();
disp('El servidor est? en funcionamiento.');

% Espera a que se presione Ctrl+C para detener el servidor
disp('Presione Ctrl+C para detener el servidor.');
pause;
disp('El servidor se ha detenido.');

% Det?n el servidor
server.stop();


% Mueve todas las declaraciones antes de la definici?n de la funci?n
% Define una funci?n de controlador para manejar la solicitud GET
function response = handleGetRequest(~, ~)
    % Aqu? puedes realizar cualquier procesamiento necesario y generar la respuesta
    data = struct('message', '?Hola desde el servidor de MATLAB!');
    
    % Crea una respuesta HTTP con los datos procesados
    response = matlab.net.http.ResponseMessage(...
        matlab.net.http.Status.OK, data);
end