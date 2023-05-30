package Classes;

public class Usuario {
    private String login;
    private String nome;
    private String senha;
    private String CPF;
    private String email;

    public Usuario(String login, String nome, String senha, String CPF, String email) {
        this.login = login;
        this.nome = nome;
        this.senha = senha;
        this.CPF = CPF;
        this.email = email;
    }

    // Métodos getters e setters

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getCPF() {
        return CPF;
    }

    public void setCPF(String CPF) {
        this.CPF = CPF;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}

