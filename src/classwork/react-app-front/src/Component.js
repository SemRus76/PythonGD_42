'use client'

import react, {useState, useEffect} from 'react';
import axios from 'axios';

export default function PageFunc()
{
     
  const [formData, setFormData] = useState();
  const [helloData, setHelloData] = useState();

  function onChange(event)
  {
    setFormData(event.target.value);
  }

  const handleSubmit = () => 
    {
        axios.post('http://127.0.0.1:8000/players',{name:formData})
        .then((response) => setHelloData(response['helloName']))
        .catch((error) => (console.log('Ошибка: ', error)))
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
