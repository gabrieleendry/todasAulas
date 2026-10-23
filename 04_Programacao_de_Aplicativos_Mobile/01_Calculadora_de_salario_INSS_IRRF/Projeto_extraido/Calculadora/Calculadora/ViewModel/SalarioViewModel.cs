using System.ComponentModel;
using System.Globalization;
using System.Runtime.CompilerServices;
using System.Windows.Input;
using Microsoft.Maui.Controls;
using Calculadora.Model;

namespace Calculadora.ViewModel;

public class SalarioViewModel : INotifyPropertyChanged
{
    private readonly Salario _salario = new Salario();
    private decimal _salarioCalculado;

    public ICommand CalcularSalarioCommand { get; }

    public SalarioViewModel()
    {
        CalcularSalarioCommand = new Command(
            execute: () => CalcularSalario(),
            canExecute: () => PodeCalcular()
        );

        _valorHoraString = string.Empty;
        _horasTrabalhadasString = string.Empty;
    }

    private string _valorHoraString;
    public string ValorHoraString
    {
        get => _valorHoraString;
        set
        {
            if (_valorHoraString != value)
            {
                _valorHoraString = value;
                OnPropertyChanged();

                if (TryParseDecimal(value, out var parsed))
                    _salario.ValorHora = parsed;
                else
                    _salario.ValorHora = 0m;

                ((Command)CalcularSalarioCommand).ChangeCanExecute();
                OnPropertyChanged(nameof(SalarioCalculado));
            }
        }
    }

    private string _horasTrabalhadasString;
    public string HorasTrabalhadasString
    {
        get => _horasTrabalhadasString;
        set
        {
            if (_horasTrabalhadasString != value)
            {
                _horasTrabalhadasString = value;
                OnPropertyChanged();

                if (TryParseDecimal(value, out var parsed))
                    _salario.HorasTrabalhadas = parsed;
                else
                    _salario.HorasTrabalhadas = 0m;

                ((Command)CalcularSalarioCommand).ChangeCanExecute();
                OnPropertyChanged(nameof(SalarioCalculado));
            }
        }
    }

    public decimal SalarioCalculado
    {
        get => _salarioCalculado;
        private set
        {
            if (_salarioCalculado != value)
            {
                _salarioCalculado = value;
                OnPropertyChanged();
            }
        }
    }

    private void CalcularSalario()
    {
        SalarioCalculado = _salario.CalcularSalario();
    }

    private bool PodeCalcular()
    {
        return _salario.ValorHora > 0m && _salario.HorasTrabalhadas > 0m;
    }

    private bool TryParseDecimal(string s, out decimal result)
    {
        result = 0m;
        if (string.IsNullOrWhiteSpace(s))
            return false;

        if (decimal.TryParse(s, NumberStyles.Number, CultureInfo.CurrentCulture, out result))
            return true;

        if (decimal.TryParse(s, NumberStyles.Number, CultureInfo.InvariantCulture, out result))
            return true;

        var cleaned = s.Trim();
        return decimal.TryParse(cleaned, NumberStyles.Number, CultureInfo.CurrentCulture, out result)
            || decimal.TryParse(cleaned, NumberStyles.Number, CultureInfo.InvariantCulture, out result);
    }

    public event PropertyChangedEventHandler PropertyChanged;
    protected void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
}