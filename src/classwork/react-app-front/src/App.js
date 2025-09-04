import logo from './logo.svg';
import './App.css';
import react, {useState, useEffect} from 'react';

function App() {

  const [formData, setFormData] = useState();
  const [helloData, setHelloData] = useState();

  function onChange(event)
  {
    setFormData(event.target.value);
  }

  const handleSubmit = () => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/sayhello'); // Example API
                // if (!response.ok) {
                //     throw new Error(`HTTP error! status: ${response.status}`);
                // }
                const result = await response.json();
                setHelloData(result["name"]);
            } catch (err) {
                // setError(err);
                console.log(err);
            } finally {
                // setLoading(false);
                console.log(false);
            }
        };

        fetchData();
    };

  // function handleSubmit(event)
  // {
  //   event.preventDefault(); // блокируем стандартную отправку формы
  //   // console.log("Name: ", formData);

  // }

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <h1>
            <label>
              {helloData}
            </label>
          </h1>
        </div>
        <form onSubmit={handleSubmit}>
          <p>
              <label>Имя:</label><br />
              <input type="text" value={formData} onChange={onChange}/>
          </p>
          <input type="submit" value="Отправить" />
        </form>
      </header>
    </div>
  );
}

export default App;
