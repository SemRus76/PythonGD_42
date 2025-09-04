import Image from "next/image";
import styles from "./page.module.css";
// import { useState } from "react/cjs/react.production";
import react, {useState} from "react";

export default function Home() {

  const [formData, setFormData] = useState('');

  function onChange(event)
  {
    setFormData(event.target.value);
  }

  function sendForm(event)
  {
    event.preventDefault();
    // отправка формы
  }

  return (
      <div>
        <form onSubmit={sendForm}>
          <p>
              <label>Имя:</label><br />
              <input type="text" value={valueField} onChange={onChange}/>
          </p>
          <input type="submit" value="Отправить" />
        </form>
      </div>
  );
}
