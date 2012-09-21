import org.python.core.PyException;
import org.python.util.PythonInterpreter;

public class Main {
    public static void main(String[] args) throws PyException{
	PythonInterpreter intrp = new PythonInterpreter();
	
	//Ammend Python Module Search Path
	intrp.exec("import sys");
	intrp.exec("sys.path.append(\"__pyclasspath__/lib/modules.jar\")");
	
	intrp.exec("import JythonApplication");
	//intrp.exec("TaskBar.TrayApp()");
    }
}
