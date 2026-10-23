namespace Calculadora.Model;

public class Salario
{
    public decimal ValorHora { get; set; }
    public decimal HorasTrabalhadas { get; set; }

    public decimal CalcularSalarioBruto()
    {
        return ValorHora * HorasTrabalhadas;
    }

    public decimal CalcularINSS(decimal salarioBruto)
    {
        if (salarioBruto <= 1518.00m)
            return (salarioBruto * 0.075m) - 0m;
        if (salarioBruto <= 2793.88m)
            return (salarioBruto * 0.09m) - 22.77m;
        if (salarioBruto <= 4190.83m)
            return (salarioBruto * 0.12m) - 106.60m;
        if (salarioBruto <= 8157.41m)
            return (salarioBruto * 0.14m) - 190.42m;

        return (8157.41m * 0.14m) - 190.42m;
    }

    public decimal CalcularIRRF(decimal baseCalculo)
    {
        if (baseCalculo <= 2428.80m)
            return 0m;
        if (baseCalculo <= 2826.65m)
            return (baseCalculo * 0.075m) - 182.16m;
        if (baseCalculo <= 3751.05m)
            return (baseCalculo * 0.15m) - 394.16m;
        if (baseCalculo <= 4664.68m)
            return (baseCalculo * 0.225m) - 675.49m;

        return (baseCalculo * 0.275m) - 908.73m;
    }

    public decimal CalcularSalario()
    {
        decimal salarioBruto = CalcularSalarioBruto();
        decimal descontoINSS = CalcularINSS(salarioBruto);
        decimal baseIRRF = salarioBruto - descontoINSS;
        decimal descontoIRRF = CalcularIRRF(baseIRRF);

        return salarioBruto - descontoINSS - descontoIRRF;
    }
}