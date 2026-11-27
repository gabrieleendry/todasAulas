create database Oficinas;
use Oficinas;

CREATE TABLE OficinaSabatina (
    Id INT PRIMARY KEY,
    NomeOficina VARCHAR(100),
    Tutor VARCHAR(100),
    Sala VARCHAR(30),
    VagasMaximas INT,
    TotalInscritos INT,
    Lotada BIT);

INSERT INTO OficinaSabatina (Id, NomeOficina, Tutor, Sala, VagasMaximas, TotalInscritos, Lotada)
VALUES
(1, 'Reforco de Matematica', 'Ana', 'Lab 1', 20, 0, 0),
(2, 'Redacao', 'Bruno', 'Sala 3', 15, 14, 0),
(3, 'Programacao', 'Carla', 'Lab 2', 10, 10, 1),
(4, 'Fisica', 'Daniel', 'Lab 1', 25, 5, 0);

exec sp_help OficinaSabatina;


-- 1) Procedure sem parametro: lista tudo, com as vagas restantes
CREATE PROCEDURE sp_ListarOficinas
AS BEGIN
    SELECT Id, NomeOficina, Tutor, Sala, VagasMaximas, TotalInscritos,
           VagasMaximas - TotalInscritos AS VagasRestantes, Lotada
    FROM OficinaSabatina;
END;

exec sp_ListarOficinas;


-- 2) Procedure com parametro: lista por tutor
CREATE PROCEDURE sp_ListarPorTutor
    @Tutor VARCHAR(100)
AS BEGIN
    SELECT Id, NomeOficina, Tutor, Sala, VagasMaximas, TotalInscritos
    FROM OficinaSabatina
    WHERE Tutor = @Tutor;
END;

exec sp_ListarPorTutor @Tutor = 'Ana';
exec sp_ListarPorTutor 'Bruno';


-- 3) Procedure com parametro: lista so oficinas com vaga
CREATE PROCEDURE sp_ListarComVagas
    @Sala VARCHAR(30)
AS BEGIN
    SELECT Id, NomeOficina, Tutor, Sala,
           VagasMaximas - TotalInscritos AS VagasRestantes
    FROM OficinaSabatina
    WHERE Sala = @Sala
      AND Lotada = 0;
END;

exec sp_ListarComVagas 'Lab 1';


-- 4) Procedure de inscricao (regra de negocio simples)
CREATE PROCEDURE sp_InscreverAluno
    @Id INT
AS BEGIN
    -- soma 1 inscrito, mas so se ainda tiver vaga
    UPDATE OficinaSabatina
    SET TotalInscritos = TotalInscritos + 1
    WHERE Id = @Id
      AND Lotada = 0
      AND TotalInscritos < VagasMaximas;

    -- fecha a turma se chegou no limite
    UPDATE OficinaSabatina
    SET Lotada = 1
    WHERE Id = @Id
      AND TotalInscritos >= VagasMaximas;

    -- mostra como a oficina ficou
    SELECT Id, NomeOficina, VagasMaximas, TotalInscritos, Lotada
    FROM OficinaSabatina
    WHERE Id = @Id;
END;

exec sp_InscreverAluno @Id = 1;   -- soma 1 inscrito
exec sp_InscreverAluno 2;         -- era 14/15, agora 15/15 e fica lotada
exec sp_InscreverAluno 2;         -- ja lotada: nada muda
exec sp_InscreverAluno 3;         -- ja lotada: nada muda
