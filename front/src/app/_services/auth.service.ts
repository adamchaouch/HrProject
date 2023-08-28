import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

const AUTH_API = '';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor(private http: HttpClient) {}

  login(email: string, password: string): Observable<any> {
    return this.http.post(
      AUTH_API + 'signin',
      {
        email,
        password,
      },
      httpOptions
    );
  }

  register(username: string, email: string, password: string, confirmPassword : string, profil : string): Observable<any> {
    return this.http.post(
      AUTH_API + 'signup',
      {
        email,
        password,
        confirmPassword,
        profil,
      },
      httpOptions
    );
  }

  logout(): Observable<any> {
    return this.http.post(AUTH_API + 'signout', { }, httpOptions);
  }
}